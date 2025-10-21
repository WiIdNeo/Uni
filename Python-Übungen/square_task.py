pic = [[0, 0, 1, 1, 0, 0],[0, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 0],[0, 0, 1, 1, 0, 0]]
counter = 0
Vierx4_counter = 0
Dreix3_counter = 0
zweix2_counter = 0
einsx1_counter = 0
i = 0
for i in range(len(pic)):
    k = pic[i]
    for j in range(len(k)):
        m = k[j]
        if m == 1:
            counter+=1
            einsx1_counter+=1
print("1x1-Quadrate " + str(einsx1_counter))

for i in range(len(pic)):
    k = pic[i]
    try:
        n = pic[i+1]
    except IndexError:
        continue
    for j in range(len(k)):
        m = k[j]
        if m == 1:
            try:
                if k[j+1] == 1:
                    if n[j] == 1:
                        try:
                            if n[j+1] == 1:
                                counter+=1
                                zweix2_counter+=1
                        except IndexError:
                            continue
            except IndexError:
                continue
                
print("2x2-Quadrate " + str(zweix2_counter))
                        
for i in range(len(pic)):
    k = pic[i]
    try:
        n = pic[i+1]
    except IndexError:
        continue
    try:
        p = pic[i+2]
    except IndexError:
        continue
    for j in range(len(k)):
        m = k[j]
        if m == 1:
            try:
                if k[j+1] == 1:
                    if n[j] == 1:
                        try:
                            if n[j+1] == 1:
                                try:
                                    if k[j+2] == 1:
                                        try:
                                            if n[j+2] == 1:
                                                if p[j] == 1:
                                                    try:
                                                        if p[j+1] == 1:
                                                            try:
                                                                if p[j+2] == 1:
                                                                     counter+=1
                                                                     Dreix3_counter+=1
                                                            except IndexError:
                                                               continue
                                                    except IndexError:
                                                        continue
                                        except IndexError:
                                            continue
                                except IndexError:
                                    continue
                        except IndexError:
                            continue
            except IndexError:
                continue
print("3x3-Quadrate " + str(Dreix3_counter))


for i in range(len(pic)):
    k = pic[i]
    try:
        n = pic[i+1]
    except IndexError:
        continue
    try:
        p = pic[i+2]
    except IndexError:
        continue
    try:
        o = pic[i+3]
    except IndexError:
        continue
    for j in range(len(k)):
        m = k[j]
        if m == 1:
            try:
                if k[j+1] == 1:
                    if n[j] == 1:
                        try:
                            if n[j+1] == 1:
                                try:
                                    if k[j+2] == 1:
                                        try:
                                            if n[j+2] == 1:
                                                if p[j] == 1:
                                                    try:
                                                        if p[j+1] == 1:
                                                            try:
                                                                try:
                                                                    if p[j+2] == 1:
                                                                        try:
                                                                            if k[j+3]==1:
                                                                                try:
                                                                                    if n[j+3] == 1:
                                                                                        if o[j] == 1:
                                                                                            try:
                                                                                                if o[j+1] == 1:
                                                                                                    try:
                                                                                                        if o[j+2] == 1:
                                                                                                            try:
                                                                                                                if o[j+3] == 1:
                                                                                                                    counter+=1
                                                                                                                    Vierx4_counter+=1
                                                                                                            except IndexError:
                                                                                                                continue
                                                                                                    except IndexError:
                                                                                                        continue
                                                                                            except IndexError:
                                                                                                continue
                                                                                except IndexError:
                                                                                    continue
                                                                        except IndexError:
                                                                            continue
                                                                except IndexError:
                                                                    continue     
                                                            except IndexError:
                                                               continue
                                                    except IndexError:
                                                        continue
                                        except IndexError:
                                            continue
                                except IndexError:
                                    continue
                        except IndexError:
                            continue
            except IndexError:
                continue
print("4x4-Quadrate " + str(Vierx4_counter))
print("Insgesamt: " + str(counter))