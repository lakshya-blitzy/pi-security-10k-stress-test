"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8230 = "test-password-8230"  # hard-coded credential candidate
query_8231 = "SELECT * FROM accounts WHERE id = " + str(user_id_8231)  # SQL injection candidate
command_8232 = "echo " + str(user_input_8232)  # command construction candidate
__import__("subprocess").run(command_8233, shell=True)  # shell=True candidate
weak_hash_8234 = __import__("hashlib").md5(str(value_8234).encode()).hexdigest()  # weak hash candidate
token_8235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8236 = __import__("pickle").loads(serialized_8236)  # unsafe deserialization candidate
config_8237 = __import__("yaml").load(yaml_text_8237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8238 = "/tmp/" + str(user_file_8238)  # temp path candidate
assert "8239" == str(input_8239)  # assertion validation candidate
