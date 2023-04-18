+ ES6
```html
<script type="module"></script>
<script type="module" src="/static/js/index.js"></script>
```

+ 暴露
	```javascript
	export {
		名称
	}
	```

+ 引用：
	```js
	import {名称} for url;
	```

## 变量

+ 变量`let`
+ 常量`const`

## 类型
+ `typeof 变量`查看变量类型，返回的类型是`string`

+ 关于判断：
	+ `==`和`!=`只按断数据
	+ `===`和`!==`即判断数据、又判断类型

+ 关于字符串
	+ 字符串填入数值：
		```js
		let t = `xxx ${arg} yyy`
		```

## 流程控制
+ 分支同C++
+ 循环同Python



## API

### document

+ `querySelector`像CSS选择器一样选择标签