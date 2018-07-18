class Entry:
    def __init__(self):
        pass

    entries = [
        {
            'id': 1,
            'title': 'Nibh praesent tristique magna sit',
            'body': (
                'At risus viverra adipiscing at in. Aliquet eget sit amet tellus. Facilisis mauris sit amet massa '
                'vitae tortor condimentum lacinia. Gravida neque convallis a cras semper auctor neque vitae. '
                'Facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum. Aliquet porttitor lacus '
                'luctus accumsan tortor posuere. Facilisis magna etiam tempor orci. Pellentesque pulvinar '
                'pellentesque habitant morbi tristique senectus. Tortor at auctor urna nunc id cursus metus '
                'aliquam. Tellus elementum sagittis vitae et leo duis ut diam quam. Ullamcorper a lacus vestibulum '
                'sed arcu. Ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit. Nunc '
                'mattis enim ut tellus elementum. Pellentesque habitant morbi tristique senectus et netus. Purus '
                'viverra accumsan in nisl nisi scelerisque eu ultrices.'
            )
        },
        {
            'id': 2,
            'title': 'Praesent semper feugiat nibh sed',
            'body': (
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                'labore et dolore magna aliqua. Neque viverra justo nec ultrices dui sapien eget mi proin. Nisl '
                'vel pretium lectus quam id leo in vitae turpis. Tincidunt ornare massa eget egestas purus viverra '
                'accumsan in nisl. Tempus egestas sed sed risus pretium. Commodo nulla facilisi nullam vehicula '
                'ipsum a. Dignissim sodales ut eu sem integer vitae justo. Eleifend quam adipiscing vitae proin '
                'sagittis nisl rhoncus mattis. Eu mi bibendum neque egestas congue quisque. Neque aliquam '
                'vestibulum morbi blandit cursus. Tellus pellentesque eu tincidunt tortor. Potenti nullam ac '
                'tortor vitae purus faucibus ornare suspendisse.'
            )
        },
        {
            'id': 3,
            'title': 'Eu scelerisque felis imperdiet proin',
            'body': (
                'Vulputate dignissim suspendisse in est. Faucibus et molestie ac feugiat sed lectus vestibulum. '
                'Molestie a iaculis at erat. Augue eget arcu dictum varius. In arcu cursus euismod quis viverra '
                'nibh cras. Facilisis mauris sit amet massa vitae. Gravida in fermentum et sollicitudin ac orci '
                'phasellus. Eget duis at tellus at urna condimentum mattis pellentesque id. Blandit volutpat '
                'maecenas volutpat blandit aliquam etiam. Sem viverra aliquet eget sit. Diam ut venenatis tellus '
                'in metus vulputate eu scelerisque felis. Leo vel fringilla est ullamcorper eget nulla facilisi '
                'etiam. Nisl rhoncus mattis rhoncus urna neque. Aliquet enim tortor at auctor urna nunc id cursus '
                'metus. Sit amet porttitor eget.'
            )
        },
        {
            'id': 4,
            'title': 'Tortor pretium viverra suspendisse potenti',
            'body': (
                'Velit laoreet id donec ultrices tincidunt arcu non sodales neque. Purus viverra accumsan in nisl '
                'nisi scelerisque eu ultrices vitae. Nullam vehicula ipsum a arcu. Neque gravida in fermentum et '
                'sollicitudin ac. In ante metus dictum at tempor commodo ullamcorper a lacus. Fames ac turpis '
                'egestas integer eget. Euismod quis viverra nibh cras pulvinar mattis. Id diam maecenas ultricies '
                'mi eget mauris pharetra. Malesuada fames ac turpis egestas integer. Mattis rhoncus urna neque '
                'viverra justo. Ornare massa eget egestas purus viverra. Consectetur purus ut faucibus pulvinar '
                'elementum integer enim neque volutpat. Eget sit amet tellus cras. Ipsum dolor sit amet '
                'consectetur adipiscing elit ut aliquam. Turpis massa sed elementum tempus egestas sed sed risus. '
                'Justo laoreet sit amet cursus sit amet dictum. Tortor aliquam nulla facilisi cras fermentum odio '
                'eu feugiat. Magna ac placerat vestibulum lectus mauris ultrices eros in. Amet est placerat in '
                'egestas erat imperdiet sed. Ultricies lacus sed turpis tincidunt id aliquet.'
            )
        },
        {
            'id': 5,
            'title': 'Tellus mauris a diam maecenas',
            'body': (
                'Amet justo donec enim diam. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras '
                'fermentum. Urna nec tincidunt praesent semper. Sagittis orci a scelerisque purus semper eget duis '
                'at. Tortor id aliquet lectus proin nibh nisl condimentum id venenatis. Neque gravida in fermentum '
                'et sollicitudin. Aliquam nulla facilisi cras fermentum. Nibh praesent tristique magna sit amet. '
                'Sit amet risus nullam eget felis eget nunc lobortis. Felis bibendum ut tristique et egestas. Nibh '
                'tortor id aliquet lectus proin. Dictumst quisque sagittis purus sit amet. Sed arcu non odio '
                'euismod lacinia. Arcu cursus vitae congue mauris rhoncus aenean vel. Odio aenean sed adipiscing '
                'diam donec. Amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Molestie a iaculis '
                'at erat pellentesque. Congue nisi vitae suscipit tellus mauris a diam maecenas sed. Nisi porta '
                'lorem mollis aliquam. Tristique senectus et netus et malesuada fames ac turpis egestas.'
            )
        }
    ]

    @staticmethod
    def all():
        """
        This function generates dummy entries. Each entry has an id, title and body.
        :rtype: list
        """
        return Entry.entries
