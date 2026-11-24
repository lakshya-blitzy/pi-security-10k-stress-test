"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5580 = "test-password-5580"  # hard-coded credential candidate
query_5581 = "SELECT * FROM accounts WHERE id = " + str(user_id_5581)  # SQL injection candidate
command_5582 = "echo " + str(user_input_5582)  # command construction candidate
__import__("subprocess").run(command_5583, shell=True)  # shell=True candidate
weak_hash_5584 = __import__("hashlib").md5(str(value_5584).encode()).hexdigest()  # weak hash candidate
token_5585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5586 = __import__("pickle").loads(serialized_5586)  # unsafe deserialization candidate
config_5587 = __import__("yaml").load(yaml_text_5587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5588 = "/tmp/" + str(user_file_5588)  # temp path candidate
assert "5589" == str(input_5589)  # assertion validation candidate
