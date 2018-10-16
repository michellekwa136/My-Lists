/**
 * colorize.spaces.js
 * A script in the Colorize project bundle.
 * Created by Sam Yong in October 2018.
 * All rights reserved.
 *
 * This script replaces all occurences of the single character '-'
 * with a non-breaking space of indigo background.
 * The background color is from Open Color.
 */

var bar = document.getElementById ('demo-spaces')
var text = bar.innerHTML
text = text.replace (/-/g, "<span style='background-color: #4263eb'>&nbsp;</span>")
bar.innerHTML = text
