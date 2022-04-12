def wall_climber(depth):
	###This function calculates the amount of days needed for a man to get out of the well. it has an input called depth that shows how deep the well is. For every morning, the man goes 8m up and in the night descends 3m. E.g. wall_climber(17) -> 3 day(s)###
	day_ascent = 8
	night_descent = 3
	counter = 0
	total_ascent = 0

	while (total_ascent + day_ascent) < depth:
		total_ascent += day_ascent
		total_ascent -= night_descent
		counter += 1
	counter += 1
	print(f"{counter} day(s)")
    #return (str(counter) + "day(s)")


wall_climber(17)
