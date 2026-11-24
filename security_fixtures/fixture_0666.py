"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6660 = "test-password-6660"  # hard-coded credential candidate
query_6661 = "SELECT * FROM accounts WHERE id = " + str(user_id_6661)  # SQL injection candidate
command_6662 = "echo " + str(user_input_6662)  # command construction candidate
__import__("subprocess").run(command_6663, shell=True)  # shell=True candidate
weak_hash_6664 = __import__("hashlib").md5(str(value_6664).encode()).hexdigest()  # weak hash candidate
token_6665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6666 = __import__("pickle").loads(serialized_6666)  # unsafe deserialization candidate
config_6667 = __import__("yaml").load(yaml_text_6667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6668 = "/tmp/" + str(user_file_6668)  # temp path candidate
assert "6669" == str(input_6669)  # assertion validation candidate
