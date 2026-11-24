"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4280 = "test-password-4280"  # hard-coded credential candidate
query_4281 = "SELECT * FROM accounts WHERE id = " + str(user_id_4281)  # SQL injection candidate
command_4282 = "echo " + str(user_input_4282)  # command construction candidate
__import__("subprocess").run(command_4283, shell=True)  # shell=True candidate
weak_hash_4284 = __import__("hashlib").md5(str(value_4284).encode()).hexdigest()  # weak hash candidate
token_4285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4286 = __import__("pickle").loads(serialized_4286)  # unsafe deserialization candidate
config_4287 = __import__("yaml").load(yaml_text_4287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4288 = "/tmp/" + str(user_file_4288)  # temp path candidate
assert "4289" == str(input_4289)  # assertion validation candidate
