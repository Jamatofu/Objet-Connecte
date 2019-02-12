from . import Tree

class ButtonNode(Tree.Tree):
    def __init__(self, buttonText, destination, id, value, autoreload="false", blockOther="null"):
        super().__init__("button")
        self.buttonText = buttonText
        self.destination = destination
        self.id = id
        self.value = value
        self.autoreload = autoreload
        self.blockOther = blockOther

    def generate(self):
        checked = ""

        if (self.value == True):
            checked = "checked"

        return """
            <div>
                <span>{}</span>
                <label class="switch">
                  <input type="checkbox"
                         id="{}"
                        onclick="updateActionneur(this, '{}', '{}', '{}', '{}');
                    blockOtherButton(this.checked, '{}')"
                    {}>
                  <span class="slider round"></span>
                </label>
            </div>
        """.format(self.buttonText,
                    self.id,
                    self.destination,
                    self.value,
                    self.id,
                    self.autoreload,
                    self.blockOther,
                    checked)
