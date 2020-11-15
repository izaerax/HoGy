# -*- coding: utf-8 -*-

import csv

# Lista dei permessi per i modelli
# 1 posto => module
# 2 posto => model
# 3 posto => dict con la seguente struttura:
#   - chiave ruolo (la stessa del dict ROLES)
#   - lista di permessi con il seguente ordine: (read, write, create, unlink)
MODELS = (
    ## ORDINATI ALFABETICAMENTE COME IN Configurazione -> Struttura database -> Modelli
    ('hogy', 'hogy.coach', {'manager': (1, 1, 1, 1)}),
    ('hogy', 'hogy.disciple', {'manager': (1, 1, 1, 1)}),

)

# Lista di ruoli
# 1 livello => chiave ruolo
# 2 livello => lista con la seguente struttura: (modulo, nome gruppo)
ROLES = {
    'manager': ('hogy', 'group_hogy_manager'),
}


def main(models, roles):
    with open('../security/ir.model.access.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ['id', 'name', 'model_id:id', 'group_id:id', 'perm_read', 'perm_write', 'perm_create', 'perm_unlink'])

        for model in models:
            module_name = model[0]
            model_name = model[1]
            model_name_underscored = model[1].replace('.', '_')
            for role_key, perms in model[2].iteritems():
                role_module = roles[role_key][0]
                role_name = roles[role_key][1]
                writer.writerow([
                    "access_%s_%s" % (model_name_underscored, role_key),
                    model_name,
                    "%s.model_%s" % (module_name, model_name_underscored),
                    "%s.%s" % (role_module, role_name),
                    perms[0], perms[1], perms[2], perms[3],
                ])


if __name__ == "__main__":
    main(MODELS, ROLES)
