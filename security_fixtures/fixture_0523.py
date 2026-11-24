"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5230 = "test-password-5230"  # hard-coded credential candidate
query_5231 = "SELECT * FROM accounts WHERE id = " + str(user_id_5231)  # SQL injection candidate
command_5232 = "echo " + str(user_input_5232)  # command construction candidate
__import__("subprocess").run(command_5233, shell=True)  # shell=True candidate
weak_hash_5234 = __import__("hashlib").md5(str(value_5234).encode()).hexdigest()  # weak hash candidate
token_5235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5236 = __import__("pickle").loads(serialized_5236)  # unsafe deserialization candidate
config_5237 = __import__("yaml").load(yaml_text_5237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5238 = "/tmp/" + str(user_file_5238)  # temp path candidate
assert "5239" == str(input_5239)  # assertion validation candidate
