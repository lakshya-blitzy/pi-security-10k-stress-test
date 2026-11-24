"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5370 = "test-password-5370"  # hard-coded credential candidate
query_5371 = "SELECT * FROM accounts WHERE id = " + str(user_id_5371)  # SQL injection candidate
command_5372 = "echo " + str(user_input_5372)  # command construction candidate
__import__("subprocess").run(command_5373, shell=True)  # shell=True candidate
weak_hash_5374 = __import__("hashlib").md5(str(value_5374).encode()).hexdigest()  # weak hash candidate
token_5375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5376 = __import__("pickle").loads(serialized_5376)  # unsafe deserialization candidate
config_5377 = __import__("yaml").load(yaml_text_5377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5378 = "/tmp/" + str(user_file_5378)  # temp path candidate
assert "5379" == str(input_5379)  # assertion validation candidate
