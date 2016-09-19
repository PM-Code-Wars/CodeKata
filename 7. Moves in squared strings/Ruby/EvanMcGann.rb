# Moves in squared strings (I):
def vert_mirror(s)
    s.split("\n").each { |x| x.reverse! }.join("\n")
end
def hor_mirror(s)
    subs = s.split("\n").reverse.join("\n")
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
def rot_90_clock(s)
    diag_1_sym(s).split("\n").map { |line| line.reverse }.join("\n")
end
def diag_1_sym(s)
    subs = s.split("\n")
    new_subs = []
    for i in 0 ... subs.length
        line = subs[i]
        new_line = ""
        for j in 0 ... line.length
            new_line += subs[j][i]
        end
        new_subs.push(new_line)
    end
    new_subs.join("\n")
end
def selfie_and_diag1(s)
    subs = s.split("\n")
    diag = diag_1_sym(s).split("\n")
    res = []
    for i in 0 ... diag.length
      res.push(subs[i] + "|" + diag[i])
    end
    res.join("\n")    
end
def oper(fct, s) 
    fct.call(s)
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
    res = []
    for i in 0 ... selfie.length
      res.push(selfie[i] + "|" + diag[i] + "|" + rot[i])
    end
    res.join("\n")
end
def oper(fct, s) 
    fct.call(s)
end
def transpose(s)
  s.split("\n").map(&:chars).transpose.map(&:join)
end
