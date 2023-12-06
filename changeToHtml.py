#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import random

path = "/home/docker-compose/nginx/html/static/saving_web"
# <meta charset="UTF-8">
#path = "C:\\study\\gitbooks\\saving_web"
tmp = '''<html><head>
<link rel="stylesheet" href="./common.css" />
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
</head><body>
<div id="content">
<div class="inputDiv">
<input type="text" onkeydown="if(event.keyCode==13) {keySearch(this)}" class="input" id="input" placeholder="Search" autocomplete="off">
</div>
<div class="clock-container">
      <div class="clock">
        <div class="needle hour"></div>
        <div class="needle minute"></div>
        <div class="needle second"></div>
        <div class="center-point"></div>
      </div>
      <div class="time"></div>
      <div class="date"></div>
    </div>
''';
for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith('.html')):
			tmp += '<p><a class="books" target="_blank" href="./'+file+'">'+file.replace(".html","")+'</a></p>'

tmp += '''</div></body></html>
<script >
(() => {
    const input = document.querySelector("input");
	input.addEventListener("blur", updateValue);	
})()
function updateValue(e){
	search(e.target.value)
}
function keySearch(e){
	search(e.value)
}
function search(txt){
	let content = document.getElementsByClassName("books")
	
	for(let i = 0 ; i < content.length; i++){
		if(content[i].innerText.toLowerCase().indexOf(txt.toLowerCase()) < 0){
			content[i].style.display = "none"
		}else{
			content[i].style.display = "block"
		}
	}
	// document.querySelector("input").value= ""
}

// 时钟
const hourEl = document.querySelector('.hour')
const minuteEl = document.querySelector('.minute')
const secondEl = document.querySelector('.second')
const timeEl = document.querySelector('.time')
const dateEl = document.querySelector('.date')

const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];


function setTime() {
    const time = new Date();
    const month = time.getMonth()
    const day = time.getDay()
    const date = time.getDate()
    const hours = time.getHours()
    const hoursForClock = hours % 12
    const minutes = time.getMinutes()
    const seconds = time.getSeconds()
    const ampm = hours >= 12 ? 'PM' : 'AM'

    hourEl.style.transform = `translate(-50%, -100%) rotate(${scale(hoursForClock, 0, 11, 0, 360)}deg)`
    minuteEl.style.transform = `translate(-50%, -100%) rotate(${scale(minutes, 0, 59, 0, 360)}deg)`
    secondEl.style.transform = `translate(-50%, -100%) rotate(${scale(seconds, 0, 59, 0, 360)}deg)`

    timeEl.innerHTML = `${hoursForClock}:${minutes < 10 ? `0${minutes}` : minutes} ${ampm}`
    dateEl.innerHTML = `${days[day]}, ${months[month]} <span class="circle">${date}</span>`
}

// StackOverflow https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers
const scale = (num, in_min, in_max, out_min, out_max) => {
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
  }

setTime()

setInterval(setTime, 1000)
</script>
'''
print(tmp)
f = open(path + '/index.htm','w')
f.write(tmp)
