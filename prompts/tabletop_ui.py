# Python 2D robot control script
import numpy as np
from prompts.lmps.cached_fs import stack_objects_in_order
from utils import put_first_on_second, get_obj_pos, parse_obj_name, parse_position, get_obj_names, say, get_corner_name, get_side_name, parse_question, is_obj_visible

objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# the yellow block on the yellow bowl.
say('Ok - putting the yellow block on the yellow bowl')
put_first_on_second('small yellow square', 'yellow bowl')
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# which block did you move.
say('I moved the yellow block')
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# move the green block to the top right corner.
say('Got it - putting the green block on the top right corner')
corner_pos = parse_position('top right corner')
put_first_on_second('small green square', corner_pos)
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# stack the blue bowl on the yellow bowl on the green block.
order_bottom_to_top = ['small green square', 'small yellow square', 'blue bowl']
say(f'Sure - stacking from top to bottom: {", ".join(order_bottom_to_top)}')
stack_objects_in_order(object_names=order_bottom_to_top)
objects = ['small cyan square', 'small white square', 'purple bowl', 'small blue square', 'blue bowl', 'white bowl']
# make a triangle of blocks in the middle.
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
triangle_pts = parse_position(f'a triangle with size 10cm around the middle with {len(block_names)} points')
say('Making a triangle of blocks around the middle of the workspace')
for block_name, pt in zip(block_names, triangle_pts):
  put_first_on_second(block_name, pt)
objects = ['small cyan square', 'small white square', 'purple bowl', 'small blue square', 'blue bowl', 'white bowl']
# make the triangle smaller.
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
triangle_pts = parse_position(f'a triangle with size 5cm around the middle with {len(block_names)} points')
say('Making the triangle smaller')
for block_name, pt in zip(block_names, triangle_pts):
  put_first_on_second(block_name, pt)
objects = ['small cyan square', 'small white square', 'cyan bowl', 'small blue square', 'blue bowl', 'white bowl']
# move the cyan block into its corresponding bowl.
matches = {'small cyan square': 'cyan bowl'}
say('Got it - placing the cyan block on the cyan bowl')
for first, second in matches.items():
  put_first_on_second(first, get_obj_pos(second))
objects = ['small cyan square', 'small white square', 'cyan bowl', 'small blue square', 'blue bowl', 'white bowl']
# make a line of blocks on the right side.
say('No problem! Making a line of blocks on the right side')
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
line_pts = parse_position(f'a 30cm vertical line on the right with {len(block_names)} points')
for block_name, pt in zip(block_names, line_pts):
  put_first_on_second(block_name, pt)
objects = ['small yellow square', 'small red square', 'yellow bowl', 'small gray square', 'gray bowl', 'red bowl']
# put the small banana colored thing in between the blue bowl and green block.
say('Sure thing - putting the yellow block between the blue bowl and the green block')
target_pos = parse_position('a point in the middle betweeen the blue bowl and the green block')
put_first_on_second('small yellow square', target_pos)
objects = ['small yellow square', 'small red square', 'yellow bowl', 'small gray square', 'gray bowl', 'red bowl']
# can you cut the bowls in half.
say('no, I can only move objects around')
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small gray square', 'gray bowl', 'green bowl']
# stack the blocks on the right side with the gray one on the bottom.
say('Ok. stacking the blocks on the right side with the gray block on the bottom')
right_side = parse_position('the right side')
put_first_on_second('small gray square', right_side)
order_bottom_to_top = ['small gray square', 'small green square', 'small yellow square']
stack_objects_in_order(object_names=order_bottom_to_top)
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# hide the blue bowl.
bowl_name = np.random.choice(['yellow bowl', 'green bowl'])
say(f'Sounds good! Hiding the blue bowl under the {bowl_name}')
put_first_on_second(bowl_name, 'blue bowl')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# stack everything with the green block on top.
say('Ok! Stacking everything with the green block on the top')
order_bottom_to_top = ['blue bowl', 'pink bowl', 'green bowl', 'small pink square', 'small blue square', 'small green square']
stack_objects_in_order(object_names=order_bottom_to_top)
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# move the grass-colored bowl to the left.
say('Sure - moving the green bowl left by 10 centimeters')
left_pos = parse_position('a point 10cm left of the green bowl')
put_first_on_second('green bowl', left_pos)
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# why did you move the red bowl.
say(f'I did not move the red bowl')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# undo that.
say('Sure - moving the green bowl right by 10 centimeters')
left_pos = parse_position('a point 10cm right of the green bowl')
put_first_on_second('green bowl', left_pos)
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# place the top most block to the corner closest to the bottom most block.
top_block_name = parse_obj_name('top most block', f'objects = {get_obj_names()}')
bottom_block_name = parse_obj_name('bottom most block', f'objects = {get_obj_names()}')
closest_corner_pos = parse_position(f'the corner closest to the {bottom_block_name}', f'objects = {get_obj_names()}')
say(f'Putting the {top_block_name} on the {get_corner_name(closest_corner_pos)}')
put_first_on_second(top_block_name, closest_corner_pos)
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# move the brown bowl to the side closest to the green block.
closest_side_position = parse_position('the side closest to the green block')
say(f'Got it - putting the brown bowl on the {get_side_name(closest_side_position)}')
put_first_on_second('brown bowl', closest_side_position)
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# place the green block to the right of the bowl that has the blue block.
bowl_name = parse_obj_name('the bowl that has the blue block', f'objects = {get_obj_names()}')
if bowl_name:
  target_pos = parse_position(f'a point 10cm to the right of the {bowl_name}')
  say(f'No problem - placing the green block to the right of the {bowl_name}')
  put_first_on_second('small green square', target_pos)
else:
  say('There are no bowls that has the blue block')
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# place the blue block in the empty bowl.
empty_bowl_name = parse_obj_name('the empty bowl', f'objects = {get_obj_names()}')
if empty_bowl_name:
  say(f'Ok! Putting the blue block on the {empty_bowl_name}')
else:
  say('There are no empty bowls')
put_first_on_second('small blue square', empty_bowl_name)
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# move the other blocks to the bottom corners.
block_names = parse_obj_name('blocks other than the blue block', f'objects = {get_obj_names()}')
corners = parse_position('the bottom corners')
for block_name, pos in zip(block_names, corners):
  put_first_on_second(block_name, pos)
objects = ['brown bowl', 'small green square', 'small brown square', 'green bowl', 'blue bowl', 'small blue square']
# move the red bowl a lot to the left of the blocks.
say('Sure! Moving the red bowl to a point left of the blocks')
left_pos = parse_position('a point 20cm left of the blocks')
put_first_on_second('red bowl', left_pos)
objects = ['small pink square', 'small gray square', 'small orange square']
# move the pinkish colored block on the bottom side.
say('Ok - putting the pink block on the bottom side')
bottom_side_pos = parse_position('the bottom side')
put_first_on_second('small pink square', bottom_side_pos)
objects = ['yellow bowl', 'small blue square', 'small yellow square', 'blue bowl']
# is the blue block to the right of the yellow bowl?
if parse_question('is the blue block to the right of the yellow bowl?', f'objects = {get_obj_names()}'):
  say('yes, there is a blue block to the right of the yellow bow')
else:
  say('no, there is\'t a blue block to the right of the yellow bow')
objects = ['yellow bowl', 'small blue square', 'small yellow square', 'blue bowl']
# how many yellow objects are there?
n_yellow_objs = parse_question('how many yellow objects are there', f'objects = {get_obj_names()}')
say(f'there are {n_yellow_objs} yellow object')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# move the left most block to the green bowl.
left_block_name = parse_obj_name('left most block', f'objects = {get_obj_names()}')
say(f'Moving the {left_block_name} on the green bowl')
put_first_on_second(left_block_name, 'green bowl')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# move the other blocks to different corners.
block_names = parse_obj_name(f'blocks other than the {left_block_name}', f'objects = {get_obj_names()}')
corners = parse_position('the corners')
say(f'Ok - moving the other {len(block_names)} blocks to different corners')
for block_name, pos in zip(block_names, corners):
  put_first_on_second(block_name, pos)
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# is the pink block on the green bowl.
if parse_question('is the pink block on the green bowl', f'objects = {get_obj_names()}'):
  say('Yes - the pink block is on the green bowl.')
else:
  say('No - the pink block is not on the green bowl.')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# what are the blocks left of the green bowl.
left_block_names =  parse_question('what are the blocks left of the green bowl', f'objects = {get_obj_names()}')
if len(left_block_names) > 0:
  say(f'These blocks are left of the green bowl: {", ".join(left_block_names)}')
else:
  say('There are no blocks left of the green bowl')
objects = ['small pink square', 'small green square', 'pink bowl', 'small blue square', 'blue bowl', 'green bowl']
# if you see a purple bowl put it on the blue bowl
if is_obj_visible('purple bowl'):
  say('Putting the purple bowl on the pink bowl')
  put_first_on_second('purple bowl', 'pink bowl')
else:
  say('I don\'t see a purple bowl')
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# imagine that the bowls are different biomes on earth and imagine that the blocks are parts of a building.
say('ok')
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small blue square', 'blue bowl', 'green bowl']
# now build a tower in the grasslands.
order_bottom_to_top = ['green bowl', 'small blue square', 'small green square', 'small yellow square']
say('stacking the blocks on the green bowl')
stack_objects_in_order(object_names=order_bottom_to_top)
objects = ['small yellow square', 'small green square', 'yellow bowl', 'small gray square', 'gray bowl', 'green bowl']
# show me what happens when the desert gets flooded by the ocean.
say('putting the yellow bowl on the blue bowl')
put_first_on_second('yellow bowl', 'blue bowl')
objects = ['small pink square', 'small gray square', 'small orange square']
# move all blocks 5cm to the top.
say('Ok - moving all blocks 5cm to the top')
block_names = parse_obj_name('the blocks', f'objects = {get_obj_names()}')
for block_name in block_names:
  target_pos = parse_position(f'a point 5cm above the {block_name}')
  put_first_on_second(block_name, target_pos)