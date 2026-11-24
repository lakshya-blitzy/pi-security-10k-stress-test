"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4270 = "test-password-4270"  # hard-coded credential candidate
query_4271 = "SELECT * FROM accounts WHERE id = " + str(user_id_4271)  # SQL injection candidate
command_4272 = "echo " + str(user_input_4272)  # command construction candidate
__import__("subprocess").run(command_4273, shell=True)  # shell=True candidate
weak_hash_4274 = __import__("hashlib").md5(str(value_4274).encode()).hexdigest()  # weak hash candidate
token_4275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4276 = __import__("pickle").loads(serialized_4276)  # unsafe deserialization candidate
config_4277 = __import__("yaml").load(yaml_text_4277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4278 = "/tmp/" + str(user_file_4278)  # temp path candidate
assert "4279" == str(input_4279)  # assertion validation candidate
