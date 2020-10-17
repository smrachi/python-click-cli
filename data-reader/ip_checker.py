#!/usr/bin/env python3

import click 
import re

class IPAddress(click.ParamType):
	name = "ip-address"

	def convert(self, value, param, ctx):
		regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
		found = re.search(regex, value)

		if not found:
			self.fail(
				f'{value} is not an ipv4 address.',
				param,
				ctx,
				)
		return value