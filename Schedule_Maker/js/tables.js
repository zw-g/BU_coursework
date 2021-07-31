(function(window, undefined) {
	'use strict'
	var tablep = document.getElementById('tablep');
	console.log('ok')

	/**
	 * 动态生成课程表的函数
	 * @param obj 表格元素
	 */
	function TimeTable(obj) {
		var _this = this
		var totalArr = []	//保存页面表格数据的数组
		var WEEK = 7	//星期数
		var LESSON = 10	//每日课程数
		//星期字符串数组
		var weekList = ["Sunday "," Monday ", "Tuesday "," Wednesday ", "Thursday "," Friday ", "Saturday"];
		//课程字符串数组	
		var defaultLesson = ['PE', 'Math',' English ', 'History', 'Biology', 'Chem', 'Brunch', 'Lunch', 'Break']
		//时间字符串数组		
		var time = ["8 AM","9 AM","10 AM","11 AM","12 PM","13 PM","14 PM","15 PM","16 PM","17 PM"];
		var arrObj = {}
		var dblclickListener, clickListener, editListener, defaultChooseListener
		for(var i = 0; i < LESSON; i++) {
			let needkey = 'arr' + i;
			needkey = []
			arrObj['arr' + i] = needkey
		}
		this.el = obj.el
		this.tt = {
			inits: () => { // 初始化
				this.tt._initTable() // 创建一个空白表格
				this.tt._drawTable() // 绘制表格
				this.tt._handlerClickTable() // 点击表格事件
			},
			_initTable: () => { // 创建一个新的空白课程表

				for(let i = 0; i < LESSON; i++) {
					let itemArr = new Array(WEEK)
					for(let j = 0; j < WEEK; j++) {
						itemArr[j] = '' + i + j
					}
					totalArr.push(itemArr)
				}
			},
			_drawTable: () => { // 绘制表格
				var htmlstr = '<table class="wxtable table table-bordered">'

				/* 开始绘制表头 */
				htmlstr += '<thead class="wxtable-thead"><tr class="wxtable-thead-tr">'
				for(let i = 0; i < WEEK+1; i++) {
					//如果是第一行第一列，不绘制内容
					if(i==0){
						htmlstr += '<td class="wxtable-thead-td">'
						htmlstr += '</td>'
					}else{
						htmlstr += '<td class="wxtable-thead-td">'
						htmlstr += weekList[i-1];
						htmlstr += '</td>'
						
					}
				}
				htmlstr += '</tr></thead>'
				/* 表头绘制结束 */

				/* 开始绘制表格内容 */
				htmlstr += '<tbody class="wxtable-tbody">'
				for(let i = 0; i < LESSON; i++) {
					htmlstr += '<tr class="wxtable-tbody-tr">'
					let item = totalArr[i];
					for(let j = 0; j < WEEK+1; j++) {
						
						htmlstr += '<td class="wxtable-tbody-td">'
						htmlstr += '<span class="text-span">'
						//如果是每一行的第一列，绘制上课时间，其余绘制课程内容
						if(j==0){
							htmlstr +=time[i]
						}else{
							htmlstr += ''
						}
						htmlstr += '</span>'
						htmlstr += '<div class="wxtable-tbody-changeBox">'
						htmlstr += '<div class="defaultChoose">'
						for(let i = 0; i < defaultLesson.length; i++) {
							htmlstr += '<em class="label label-primary defaultItem">' + defaultLesson[i] + '</em>'
						}
						htmlstr += '</div>'
						htmlstr += '<input value="" class=" form-control wxtable-tbody-input">'
						htmlstr += '<div class="btn-area"><button class="btn-commit btn btn-success"><svg t="1539141391804" class="icon" style="" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1595" xmlns:xlink="http://www.w3.org/1999/xlink" width="16" height="16"><defs><style type="text/css"></style></defs><path d="M107.989567 530.065291c0 0 145.950931 134.73905 252.219214 291.304222 216.422246-360.877031 549.425126-558.767337 549.425126-558.767337s27.354287-85.79299-30.638234-56.645785c0 0-236.299899 99.316631-538.515135 368.872506-103.129652-99.467064-162.839363-124.280359-162.839363-124.280359C102.981266 414.454797 107.989567 530.065291 107.989567 530.065291z" p-id="1596" fill="#ffffff"></path></svg></button><button class="btn-cancel btn btn-danger"><svg t="1539141420964" class="icon" style="" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2452" xmlns:xlink="http://www.w3.org/1999/xlink" width="16" height="16"><defs><style type="text/css"></style></defs><path d="M562.9 512l386.5-386.5c14.1-14.1 14.1-36.9 0-50.9-14.1-14.1-36.9-14.1-50.9 0L512 461.1 125.5 74.5c-14.1-14.1-36.9-14.1-50.9 0-14.1 14.1-14.1 36.9 0 50.9L461.1 512 74.5 898.5c-14.1 14.1-14.1 36.9 0 50.9 7 7 16.2 10.5 25.5 10.5s18.4-3.5 25.5-10.5L512 562.9l386.5 386.5c7 7 16.2 10.5 25.5 10.5s18.4-3.5 25.5-10.5c14.1-14.1 14.1-36.9 0-50.9L562.9 512z" p-id="2453" fill="#ffffff"></path></svg></button></div>'
						htmlstr += '<div class="triangle_border_down"><span></span></div>'
						htmlstr += '</div>'
						htmlstr += '</td>'
					}
					htmlstr += '</tr>'
				}
				htmlstr += '</tbody>'
				/* 表格内容绘制结束*/

				htmlstr += '</table>'
				tablep.innerHTML = htmlstr
			},
			_handlerClickTable: () => { // 点击事件处理
				var _this = this

				dblclickListener = tablep.addEventListener('click', (e) => { // 双击开启修改框
					e.stopPropagation();
					let tds = tablep.getElementsByClassName('wxtable-tbody-td');
					let tar = e.target;
					let bak = tar.innerText;
					/*只有在表格内容处双击，才能触发双击事件*/
					if(e.target.className === 'wxtable-tbody-changeBox' || e.target.className === 'wxtable-tbody-input' || e.target.className === 'btn-area' || e.target.className === 'btn-commit' || e.target.className === 'btn-cancel') {} else {
						for(var i = 0; i < tds.length; i++) {
							let item = tds[i];
							let tarEl = item.getElementsByClassName('wxtable-tbody-changeBox')[0]
							tarEl.style.display = 'none';
						}
					}
					if(e.target.className === 'wxtable-tbody-td') {
						for(var i = 0; i < tds.length; i++) {
							let item = tds[i];
							let tarEl = item.getElementsByClassName('wxtable-tbody-changeBox')[0]
							
							tarEl.style.display = 'none';
						}
						let tarEl = tar.getElementsByClassName('wxtable-tbody-changeBox')[0]
						let tarInput = tarEl.getElementsByClassName('wxtable-tbody-input')[0]
						setTimeout(() => {
							tarInput.focus();
						}, 10);
						tarEl.style.display = 'block';
					} else if(e.target.className === 'text-span') {
						for(var i = 0; i < tds.length; i++) {
							let item = tds[i];
							let tarEl = item.getElementsByClassName('wxtable-tbody-changeBox')[0]

							tarEl.style.display = 'none';
						}
						let tars = tar.parentNode;
						let tarEl = tars.getElementsByClassName('wxtable-tbody-changeBox')[0]
						let tarInput = tarEl.getElementsByClassName('wxtable-tbody-input')[0]
						tarInput.value = bak
						setTimeout(() => {
							tarInput.focus();
						}, 10);
						tarEl.style.display = 'block';
					}
				}, false);

				clickListener = tablep.addEventListener('click', (e) => { // 取消修改
					let tar = e.target
					let tds = tablep.getElementsByClassName('wxtable-tbody-td');

					if(tar.className === 'btn-cancel btn btn-danger' || (tar.tagName === 'svg' && tar.parentNode.className === 'btn-cancel btn btn-danger')) {
						for(var i = 0; i < tds.length; i++) {
							let item = tds[i];
							let tarEl = item.getElementsByClassName('wxtable-tbody-changeBox')[0]
							tarEl.style.display = 'none';
						}
					}
				}, true)

				/*选择好课程后，点击保存按钮，数据保存在对应数组，并展示在表格上*/
				/*选择好课程后，点击取消按钮，回复默认数据*/
				editListener = tablep.addEventListener('click', (e) => { // 修改
					let tar = e.target
					let tds = tablep.getElementsByClassName('wxtable-tbody-td');
					if(tar.className === 'btn-commit btn btn-success') {
						let tarParent = tar.parentNode.parentNode;
						let tdFather = tarParent.parentNode;
						let tarInput = tarParent.getElementsByTagName('input')[0];

						let tarValue = tarInput.value;

						let originSpan = tdFather.getElementsByTagName('span')[0];

						originSpan.innerText = tarValue;

						for(var i = 0; i < tds.length; i++) {
							let item = tds[i];
							let tarEl = item.getElementsByClassName('wxtable-tbody-changeBox')[0]
							tarEl.style.display = 'none';
						}
					} else if(tar.tagName === 'svg' && tar.parentNode.className === 'btn-commit btn btn-success') {
						
						let tarParent = tar.parentNode.parentNode.parentNode;
						let tdFather = tarParent.parentNode;
						let tarInput = tarParent.getElementsByTagName('input')[0];
						let tarValue = tarInput.value;
						let originSpan = tdFather.getElementsByTagName('span')[0];
						originSpan.innerText = tarValue;
						

						for(var i = 0; i < tds.length; i++) {
							let item = tds[i];
							let tarEl = item.getElementsByClassName('wxtable-tbody-changeBox')[0]
							tarEl.style.display = 'none';
						}
					}
				}, true)

				defaultChooseListener = tablep.addEventListener('click', (e) => { // 默认选项选择
					e.stopPropagation();
					let tar = e.target;
					let tds = tablep.getElementsByClassName('wxtable-tbody-td');
					if(tar.className === 'label label-primary defaultItem') {
						let tarText = tar.innerText;
						let tarParent = tar.parentNode.parentNode.parentNode.getElementsByClassName("text-span")[0];
						tarParent.innerText = tarText;
					}
				}, false)
			},
			resetArr: () => { // 重置数组
				for(var i in arrObj) {
					arrObj[i] = []
				}
			},
			_handlerSaver: () => { // 保存新数组
				let _this = this
				_this.tt.resetArr()
				let tds = tablep.getElementsByClassName('wxtable-tbody-td');
				let startArr = []
				let endArr = []
				for(let i = 0; i < tds.length; i++) {
					let item = tds[i]
					let tarValue = item.getElementsByTagName('span')[0].innerText;
					startArr.push(tarValue);
				}
				for(let i = 0; i < startArr.length; i++) {
					let item = startArr[i];
					// parseInt(i / 7)
					_this.tt.detailArr(parseInt(i / WEEK), item)
				}
				for(let i in arrObj) {
					endArr.push(arrObj[i])
				}

				return endArr;
			},
			detailArr: (query, value) => { // 数组处理分类
				switch(query) {
					case 0:
						arrObj.arr0.push(value)
						break;
					case 1:
						arrObj.arr1.push(value)
						break;
					case 2:
						arrObj.arr2.push(value)
						break;
					case 3:
						arrObj.arr3.push(value)
						break;
					case 4:
						arrObj.arr4.push(value)
						break;
					case 5:
						arrObj.arr5.push(value)
						break;
					case 6:
						arrObj.arr6.push(value)
						break;
					case 7:
						arrObj.arr7.push(value)
						break;
					case 8:
						arrObj.arr8.push(value)
						break;
					case 9:
						arrObj.arr9.push(value)
						break;
				}
			},
			_handlerDragger: () => { // 拖拽事件

			}
		}
		this.handlerSaver = function() {
			console.log('11')
			var arr = _this.tt._handlerSaver()
			return arr
		}
		this.tt.inits()
	}
	window.TimeTable = TimeTable
})(window, undefined)