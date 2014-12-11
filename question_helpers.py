import defs
import os

pagenum = 2
diffs = {}

def set_page(x):
	global pagenum
	pagenum = x

def set_diffs(x):
	global diffs
	diffs = x

def header():
	out = ""
	for x in open('junk'):
		print x

	print u'''
	<script type='text/javascript' src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js'></script>
<script>//written by Morris Alper -- January 2013
//you may copy with attribution

//Navigation.js: provides functionality for multi-page surveys

var current = 1; //the current page

var moved = []; //pages which have been moved by the randomization
var movedto = [];

//takes randomization into account
function effectivePage(pagenum) {
	var index = moved.indexOf(pagenum);
	if(index == -1) {
		return pagenum;
	}else{
		return movedto[index];
	}
}

var numberText = []; //stores divs which need to be updated when the page changes
var pntexts = []; //texts in them
function makePageNumber(text) { //text: something like "Page 1 / 4"
	var temp = text.split(1);
	var texts = [temp[0], temp[1]];
	//the following is needed if there are more 1's (e.g. if the total # of pages contains the digit 1)
	if(temp.length > 2) {
		for(var i = 2; i < temp.length; i++) {
			texts[1] += 1 + temp[i];
		}
	}
	document.writeln("<p><div id='pagenumberdiv" + numberText.length + "'></div></p>");
	loadPageNumber(("pagenumberdiv" + numberText.length), texts);
}
function loadPageNumber(id, texts) {
	var newone = document.getElementById(id);
	numberText.push(newone);
	pntexts.push(texts);
	updatePageNumbers();
}
function updatePageNumbers() {
	for(var i = 0; i < numberText.length; i++) {
		numberText[i].innerHTML = pntexts[i][0] + current + pntexts[i][1];
	}
}

//make one vanish and the other appear
function swap(vanish, appear) {
	document.getElementById(vanish).style.display = "none";
	//document.getElementById(appear).style.display = "inline";
	document.getElementById(appear).style.display = "";
	updatePageNumbers();
}

//go to the next page
function next() {
	current++;
	swap(effectivePage(current - 1), effectivePage(current));
}

function back() {
	current--;
	swap(effectivePage(current + 1), effectivePage(current));
}

//shuffles the array
//taken from http://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array-in-javascript
Array.prototype.shuffle = function () {
    for (var i = this.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = this[i];
        this[i] = this[j];
        this[j] = tmp;
    }

    return this;
}

//randomize the order of trials i through j
//note: don't call this on the same index twice!
function randomize(i, j) {
	ar = [];
	ar2 = [];
	for(var k = i; k <= j; k++) {
		ar.push(k);
		ar2.push(k);
	}
	ar2.shuffle();
	for(var k = 0; k < ar.length; k++) {
		if(moved.indexOf(ar[k]) != -1) {
			alert("Error: same index randomized twice.");
		}else{
			moved.push(ar[k]);
			movedto.push(ar2[k]);
		}
	}
}</script>
'''


	print '''

<style type="text/css">
.wrapper {
	height: 80%;
	width: 100%;
	display: table;
}

.page {
	display: table-cell;
	vertical-align: middle;
}

.cell {
	margin: 0 auto;
	padding: 10px;
	width: 850px;
}

#pagenum {
	text-align: center;
	font-style: italic;
}
.disclaimer {
	font-weight: bold;
	color: #555555;
}

.warning {
	font-weight: bold;
}

body {
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}
</style>

<form name='mturk_form' method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'>
  <input type='hidden' value='' name='assignmentId' id='assignmentId'/>	


<div class="wrapper">
<div class="page" id="1">
<div class="cell">

<div align="center"><h1>Vocabulary Test</h1></div>

<div class="disclaimer">Disclaimer: By answering the following questions, you are participating in a study being performed as part of a cognitive science course by a student at Indiana University.  I personally appreciate your help in completing this study!</div>
<br />

<div class="warning">Please only complete this HIT once. You will not be paid for retakes. Only the first submission of this HIT will be accepted.</div>
<br />

<p>In this study, you will be given a set of vocabulary questions that require selecting the answer most like the given word. For each question, please read all words before making a selection.</p>


<input type="button" value="Continue" onclick="next();" />

</div>
</div>
</div>
'''
	return out


def questionPage(qs):
	global pagenum
	out = ''
	head = '''<div class="wrapper">
	<div class="page" id="%d" style="display: none;">
	<div class="cell">
<h2>Vocabulary Test</h2>
<p>Please select the word which is most similar to the given word.</p>'''%pagenum
	pagenum+=1
	foot =  '''<input type="button" value="Continue" onclick="next();" />

</div>
</div>
</div>'''
	print head
	i = 0

	

	for q in qs:
		field_label = q[0]
		if field_label[:-1] in diffs:
			field_label = str(diffs[field_label[:-1]])+field_label
		quest = u'''
		<div class="cell">

	<fieldset><label><b>{0}</b></label>

	<div class="radio"><label><input name="{5}" type="radio" value="{1}" />{1} </label></div>
	<div class="radio"><label><input name="{5}" type="radio" value="{2}" />{2} </label></div>
	<div class="radio"><label><input name="{5}" type="radio" value="{3}" />{3} </label></div>
	<div class="radio"><label><input name="{5}" type="radio" value="{4}" />{4} </label></div>

	</fieldset>
	</div>'''.format(q[0][:-1],q[1][0],q[1][1],q[1][2],q[1][3],field_label)
		i+=1
		print  quest
	print  foot
	return out

import random
def definitions_page():
	global pagenum
	global diffs
	defarr = [None,defs.d0,defs.d1,defs.d2,defs.d3]
	diffarr = filter(lambda x: diffs[x] != 0, diffs)
	thisdef = random.sample(map(lambda wrd: [wrd,random.sample(defarr[diffs[wrd]][wrd],1)[0]], diffarr),8)

	for i in range(0,8,2):
		out = ''
		head = '''<div class="wrapper">
	<div class="page" id="{0}" style="display: none;">
	<div class="cell">

	<h2>Review</h2>
	<p>Please read and study the following word definitions before continuing</p>
	'''.format(pagenum)

		print  head
		pagenum+=1

		for x in thisdef[i:i+2]:
			print  '''<fieldset><label>{0}</label>
	<p>{1}</p>
	</fieldset>
	'''.format(x[0],x[1].lower())
			
		foot='''<input type="button" value="Continue" onclick="next();" />
	</div>
	</div>
	</div>'''
		print  foot

def new_defs_page(d):
	global pagenum
	out = ''
	header = '''<div class="wrapper">
<div class="page" id="{0}" style="display: none;">
<div class="cell">

<h2>Vocab</h2>
<p>Please define the following vocabulary in your own words, to help others review these words for future trials.  If you remember synonyms from the questions please do not use them in your definition</p>
'''.format(pagenum)
	pagenum+=1

	body = '''<div class="cell">
<p>{1}</p>
<textarea name="{0}" id="{0}" rows="4" cols="50"></textarea>

	</div>'''.format(d[0]+'D',d[0])

	footer = '''<input type="button" value="Continue" onclick="next();" />
</div>
</div>
</div>
'''
	print  header
	print  body
	print  footer
	return out

def demos():
	global pagenum
	out = ''
	print  '''<div class="wrapper">
	<div class="page" id="%d" style="display: none;">
<div class="cell">
<h2>Demographic Information</h2>
<p>Please help us out by answering the following questions about yourself. You must answer all of the questions marked with an asterisk (*).</p>
<p><b>*What is your gender?</b></p>
<select name="gender" id="gender">
<option selected="selected" value="default">Please select</option>
<option value="Male">Male</option>
<option value="Female">Female</option>
<option value="Other">Other</option>
</select>
<p><b>*How old are you?</b></p>
<select name="age" id="age">
<option selected="selected" value="default">Please select</option>
<script>
for (var i = 10; i < 100; i++) {
	document.writeln("<option value='" + i + "'>" + i + "</option>");
}
</script>
</select>
<script>
function fillInLanguages() {
	document.writeln(languageInputHTML);
}
</script>
<p><b>*What country are you from?</b></p>
<select name="country" id="country">
<script>document.writeln(countryInputHTML);</script>
</select>
<br />
<br />
<input type="button" value="Continue" onclick="function filledOut(id) { return document.getElementById(id).value != 'default' } if(filledOut('gender') && filledOut('age') && filledOut('country')) { next(); }else{ alert('Please answer all of the questions marked with an asterisk (*).'); }"  />

</div>
</div>
</div>'''%pagenum
	pagenum+=1
	return out

def thanks():
	global pagenum
	out =''
	print  '''<div class="wrapper">
	<div class="page" id="{0}" style="display: none;">
<div class="cell">

<p>Thank you for your help!</p>
<br />
<p><input type='submit' id='submitButton' value='Submit' /></p></form>
<script language='Javascript'>turkSetAssignmentID();</script>
</form>

</div>
</div>
</div>
</div>'''.format(pagenum)

	pagenum+=1
	return out