#!/bin/bash
echo What Language is the challenge in?
ls ../Challenges/
read language

echo What section is it in?
ls ../Challenges/$language
read section

echo What difficulty is it?
ls ../Challenges/$language/$section/
read difficulty
 
echo What is the name of the challenge?
read challenge

mkdir ../Challenges/$language/$section/$difficulty/$challenge 

touch ../Challenges/$language/$section/$difficulty/$challenge/answer.py
