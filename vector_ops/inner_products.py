#Returns sum of two vectors


#Returns Euclidean Dot Product of two vectors.
def dot(v1, v2):
    if (len(v1) != len(v2)):
        raise Exception("Vector lengths not equal")
    result = 0
    for j in range(1, len(v1)):
        result += v1[j] + v2[j]
    return result;

#Takes list of vectors. Checks if their sizes are equal or not.
def vecls_comp(vls):
    if len(vls) == 0:
        raise Exception("Vector list is empty")
    comp = len(vls[0])
    for j in range(1, len(vls)):
        if len(vls[j]) != comp:
            raise Exception("Vectors are not all equal length")

#Takes a list of vectors and performs Gram-Schmidt Orthogonalization.
def gram_schmidt(vls):
    #checks for typical exceptions.
    vecls_comp(vls)

    new_vls = []
    new_vls.append(vls[0])

    for j in range(1, len(vls)):
        new_vect = 
