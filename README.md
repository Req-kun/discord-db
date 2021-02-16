# データベースの作成

この関数はデータベースを作成する一度のみ使用  

```py
await create_db(client, channel_id, file_type)
```  

> client - commands.Bot / discord.Client  
channel_id - discord.TextChannel.id データベースとするチャンネルのID  
file_type - str / int / float / dict / list 保存したい型  

実行結果：  

```py
>>>     <message id>
```  

この数値はconnect関数を使用する際に必要です

# データベースに接続

```py
await connect(bot, channel_id, message_id)
```  

返り値を必ず受け取ってください。  
この説明では返り値をconnで表しています。  


> bot - commands.Bot / discord.Client  
channel_id - discord.TextChannel.id データベースとするチャンネルのID  
message_id - discord.Message.id create_db関数で取得した数値  

# 内容を取得

```py
await conn.content()
```

# 内容を編集

```py
await conn.edit(after_content)
```

> after_content - file_type 編集後の内容

# データベースを削除

```py
await conn.remove_db()
```
