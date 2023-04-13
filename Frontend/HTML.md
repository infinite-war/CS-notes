```html
<!DOCTYPE html><!--必须有-->
<html>
    <head>
        <title>标签的内容/搜索引擎收录的标题</title>
        <meta charset="UTF-8"><!--字符集-->
        <meta name="description" content="搜索引擎收录的描述">
        <meta name="keywords" content="搜索, 收录, 搜索的, 关键字">
        <link rel="icon" href="logo.url">
    </head>
    
    <body>
    
    </body>
</html>
```

## Tag

+ Base
	+ `div`：块状元素，默认带回车
	+ `span`：条内元素，默认不带回车
	>其他Tag都是这两种Base Tag的扩展

+ 标题：`h1`、`h2`、。。。、`h6`
+ 段落：`p`和`pre`：提供前后间距，后者等宽字体且不消除空白



+ 段落：`p`和`pre`：提供前后间距，后者等宽字体且不消除空白

  + 回车`<br>`
  + 斜体`i`
  + 加粗`b`/`strong`
  + 删除线`del`
  + 下划线`ins`
  + 标记`mark`

  ---

  + 水平线`<hr>`
  + 空格`&nbsp;`
  + 左右小括号`&lt; &gt`

---

+ 图片`img`

  + `src`属性：图片地址
  + `alt`属性：备用文本
  + `width`和`height`

+ 音频`audio`

  ```html
  <audio controls src="">无法播放</audio>
  <!--或者-->
  <audio controls><!--如果第一个无法播放则顺序播放-->
  	<source src="" type="">
  </audio>
  ```

+ 视频`video`