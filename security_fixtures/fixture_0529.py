"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5290 = "test-password-5290"  # hard-coded credential candidate
query_5291 = "SELECT * FROM accounts WHERE id = " + str(user_id_5291)  # SQL injection candidate
command_5292 = "echo " + str(user_input_5292)  # command construction candidate
__import__("subprocess").run(command_5293, shell=True)  # shell=True candidate
weak_hash_5294 = __import__("hashlib").md5(str(value_5294).encode()).hexdigest()  # weak hash candidate
token_5295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5296 = __import__("pickle").loads(serialized_5296)  # unsafe deserialization candidate
config_5297 = __import__("yaml").load(yaml_text_5297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5298 = "/tmp/" + str(user_file_5298)  # temp path candidate
assert "5299" == str(input_5299)  # assertion validation candidate
