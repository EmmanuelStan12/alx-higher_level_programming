#!/usr/bin/node
if (isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	const num = parseInt(process.argv[2]);
	for (let i = 0; i < num; i++) {
		let txt = '';
		for (let j = 0; j < num; j++) {
			txt += 'X';
		}
		console.log(txt);
	}
}
