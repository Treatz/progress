from evennia.commands.default.muxcommand import MuxCommand


class CmdLastBreath(MuxCommand):
   
    key = "+lastbreath"
    locks = "cmd:all()"

    def func(self):
        hit =  self.caller.search(self.args)
        self.caller.msg("They used to be named %s." % hit.db.lastname)
        self.caller.msg("The last person to attack %s was %s." % (hit.db.lastname, hit.db.target))
