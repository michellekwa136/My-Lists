.PHONY: courses

courses: assets/scripts/use_tag.py Courses.md
	python3 assets/scripts/use_tag.py Courses.md
