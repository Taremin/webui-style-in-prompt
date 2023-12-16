import modules.scripts as scripts
import modules.extra_networks as extra_networks
import modules.shared as shared
import gradio as gr
import re


class StyleInPrompt(scripts.Script):
    def title(self):
        return self.__class__.__name__

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion(self.title(), open=False):
            with gr.Row():
                with gr.Column(min_width=50, scale=1):
                    trigger = gr.Textbox(
                        label="Triger Word",
                        lines=1,
                        value="style",
                        interactive=True,
                        elem_id="styleinprompt_trigger_word",
                    )

        return [trigger]

    def before_process(self, p, trigger, *args, **kwargs):
        styles = shared.prompt_styles.styles
        pattern = extra_networks.re_extra_net

        def replace(prompt, is_negative=False):
            def found(m):
                name = m.group(1)
                args = m.group(2)

                if name != trigger:
                    return m.group()

                params = extra_networks.ExtraNetworkParams(items=args.split(":"))
                replace_string = ""

                for style_name in params.positional:
                    style = styles.get(style_name)
                    if style is None:
                        print(f"StyleInPrompt: style not found [{style_name}]")
                        continue
                    replace_string += (
                        style.negative_prompt if is_negative else style.prompt
                    )

                return replace_string

            while True:
                if re.search(pattern, prompt) is None:
                    break

                replaced = re.sub(pattern, found, prompt)

                if prompt == replaced:
                    break
                prompt = replaced

            return prompt

        p.prompt = replace(p.prompt, is_negative=False)
        p.negative_prompt = replace(p.negative_prompt, is_negative=True)
