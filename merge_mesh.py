search_terms = ['main', 'drone', 'done', 'foot']
containsSearchTerms = lambda x: any([y != -1 for y in [x.find(s) for s in search_terms]])

candidates = list(filter(lambda x: containsSearchTerms(x), [k for k in bpy.data.objects.keys()]))
for c in candidates:
    bpy.data.objects[c].select = True
bpy.ops.object.join()
