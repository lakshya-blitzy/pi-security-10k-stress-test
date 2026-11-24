"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4430 = "test-password-4430"  # hard-coded credential candidate
query_4431 = "SELECT * FROM accounts WHERE id = " + str(user_id_4431)  # SQL injection candidate
command_4432 = "echo " + str(user_input_4432)  # command construction candidate
__import__("subprocess").run(command_4433, shell=True)  # shell=True candidate
weak_hash_4434 = __import__("hashlib").md5(str(value_4434).encode()).hexdigest()  # weak hash candidate
token_4435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4436 = __import__("pickle").loads(serialized_4436)  # unsafe deserialization candidate
config_4437 = __import__("yaml").load(yaml_text_4437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4438 = "/tmp/" + str(user_file_4438)  # temp path candidate
assert "4439" == str(input_4439)  # assertion validation candidate
