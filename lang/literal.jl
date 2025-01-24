actual::{type} = {value};
expected::{type} = {expected};
if expected != expected
    @assert actual != actual
else
    @assert actual == expected
end
