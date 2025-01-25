def assert(cond)
  raise "(AssertionError)" unless cond;
  return
end

# NOTE: `to_f` and `to_i` truncate, so we use the actual
# type creators, `Integer` and `Float` instead.

def parse_int(str)
  return Integer(str, {base})
end

def parse_float(str)
  return Float(str)
end

actual = {parse}("{value}")
expected = {expected}
if (expected != expected) then
  assert actual != actual
else
  assert actual == expected
end
