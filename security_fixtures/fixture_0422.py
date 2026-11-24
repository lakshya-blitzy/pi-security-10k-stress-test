"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4220 = "test-password-4220"  # hard-coded credential candidate
query_4221 = "SELECT * FROM accounts WHERE id = " + str(user_id_4221)  # SQL injection candidate
command_4222 = "echo " + str(user_input_4222)  # command construction candidate
__import__("subprocess").run(command_4223, shell=True)  # shell=True candidate
weak_hash_4224 = __import__("hashlib").md5(str(value_4224).encode()).hexdigest()  # weak hash candidate
token_4225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4226 = __import__("pickle").loads(serialized_4226)  # unsafe deserialization candidate
config_4227 = __import__("yaml").load(yaml_text_4227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4228 = "/tmp/" + str(user_file_4228)  # temp path candidate
assert "4229" == str(input_4229)  # assertion validation candidate
