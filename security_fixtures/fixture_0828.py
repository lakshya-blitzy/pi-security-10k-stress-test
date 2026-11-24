"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8280 = "test-password-8280"  # hard-coded credential candidate
query_8281 = "SELECT * FROM accounts WHERE id = " + str(user_id_8281)  # SQL injection candidate
command_8282 = "echo " + str(user_input_8282)  # command construction candidate
__import__("subprocess").run(command_8283, shell=True)  # shell=True candidate
weak_hash_8284 = __import__("hashlib").md5(str(value_8284).encode()).hexdigest()  # weak hash candidate
token_8285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8286 = __import__("pickle").loads(serialized_8286)  # unsafe deserialization candidate
config_8287 = __import__("yaml").load(yaml_text_8287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8288 = "/tmp/" + str(user_file_8288)  # temp path candidate
assert "8289" == str(input_8289)  # assertion validation candidate
