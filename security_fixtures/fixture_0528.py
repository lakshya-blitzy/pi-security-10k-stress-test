"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5280 = "test-password-5280"  # hard-coded credential candidate
query_5281 = "SELECT * FROM accounts WHERE id = " + str(user_id_5281)  # SQL injection candidate
command_5282 = "echo " + str(user_input_5282)  # command construction candidate
__import__("subprocess").run(command_5283, shell=True)  # shell=True candidate
weak_hash_5284 = __import__("hashlib").md5(str(value_5284).encode()).hexdigest()  # weak hash candidate
token_5285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5286 = __import__("pickle").loads(serialized_5286)  # unsafe deserialization candidate
config_5287 = __import__("yaml").load(yaml_text_5287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5288 = "/tmp/" + str(user_file_5288)  # temp path candidate
assert "5289" == str(input_5289)  # assertion validation candidate
