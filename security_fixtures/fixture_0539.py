"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5390 = "test-password-5390"  # hard-coded credential candidate
query_5391 = "SELECT * FROM accounts WHERE id = " + str(user_id_5391)  # SQL injection candidate
command_5392 = "echo " + str(user_input_5392)  # command construction candidate
__import__("subprocess").run(command_5393, shell=True)  # shell=True candidate
weak_hash_5394 = __import__("hashlib").md5(str(value_5394).encode()).hexdigest()  # weak hash candidate
token_5395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5396 = __import__("pickle").loads(serialized_5396)  # unsafe deserialization candidate
config_5397 = __import__("yaml").load(yaml_text_5397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5398 = "/tmp/" + str(user_file_5398)  # temp path candidate
assert "5399" == str(input_5399)  # assertion validation candidate
