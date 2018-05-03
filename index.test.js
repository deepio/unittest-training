const sum = require('./index');

test('Sum function exists', () => {
  expect(sum).toBeDefined();
});

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
