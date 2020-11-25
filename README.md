# Feitify
Notify you using feishu custom bot by webhook.

## Usage
Create a `.feitifyrc` file in your home directory.
Append a JSON object like below.
```JSON
{
  "hook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/<blablabla>"
}
```

Then you can use feitify.notify to let the bot send text message.

```python
from feitify import notify
notify("hello world")
```
