"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4710 = "test-password-4710"  # hard-coded credential candidate
query_4711 = "SELECT * FROM accounts WHERE id = " + str(user_id_4711)  # SQL injection candidate
command_4712 = "echo " + str(user_input_4712)  # command construction candidate
__import__("subprocess").run(command_4713, shell=True)  # shell=True candidate
weak_hash_4714 = __import__("hashlib").md5(str(value_4714).encode()).hexdigest()  # weak hash candidate
token_4715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4716 = __import__("pickle").loads(serialized_4716)  # unsafe deserialization candidate
config_4717 = __import__("yaml").load(yaml_text_4717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4718 = "/tmp/" + str(user_file_4718)  # temp path candidate
assert "4719" == str(input_4719)  # assertion validation candidate
