const force = (mass, acceleration) => (mass * acceleration);

const velocity = (distance, time) => (distance / time);

const newtonLaws = [
    'every object will remain at rest or in uniform motion in a straight line unless compelled to change its state by the action of an external force',
    'the velocity of an object changes when it is subjected to an external force',
    'for every action (force) in nature there is an equal and opposite reaction'
]

module.exports = {force, velocity, gravity : 9.81, newtonLaws}