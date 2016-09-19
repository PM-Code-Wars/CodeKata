# Moves in squared strings (I):
def vert_mirror(s)
    s.split("\n").map(&:reverse).join("\n")
end
def hor_mirror(s)
    s.split("\n").reverse.join("\n")
end
def oper(fct, s) 
    fct.call(s)
end

# Moves in squared strings (II)
def rot(s)
    s.split("\n").map(&:reverse).reverse.join("\n")
end
def selfie_and_rot(s)
    selfie = s.split("\n").map { |line| line + ("." * line.length) }.join("\n")
    selfie + "\n" + rot(selfie)
end
def oper(fct, s) 
    fct.call(s)
end

# Moves in squared strings (III)
def diag_1_sym(s)
    transpose(s).join("\n")
end
def rot_90_clock(s)
    transpose(s).map(&:reverse).join("\n")
end
def selfie_and_diag1(s)
    s.split("\n").zip(diag_1_sym(s).split("\n")).map{|lines| lines.join("|")}.join("\n")
end
def oper(fct, s) 
    fct.call(s)
end
def transpose(s)
    s.split("\n").map(&:chars).transpose.map(&:join)
end

# Moves in squared strings (IV)
def diag_2_sym(s)
    transpose(s).map(&:reverse).reverse.join("\n")
end
def rot_90_counter(s)
    transpose(s).reverse.join("\n")
end
def selfie_diag2_counterclock(s)
    selfie = s.split("\n")
    diag = diag_2_sym(s).split("\n")
    rot = rot_90_counter(s).split("\n")
    selfie.zip(diag, rot).map{|lines| lines.join("|")}.join("\n")
end
def oper(fct, s) 
    fct.call(s)
end
def transpose(s)
  s.split("\n").map(&:chars).transpose.map(&:join)
end

