"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4580 = "test-password-4580"  # hard-coded credential candidate
query_4581 = "SELECT * FROM accounts WHERE id = " + str(user_id_4581)  # SQL injection candidate
command_4582 = "echo " + str(user_input_4582)  # command construction candidate
__import__("subprocess").run(command_4583, shell=True)  # shell=True candidate
weak_hash_4584 = __import__("hashlib").md5(str(value_4584).encode()).hexdigest()  # weak hash candidate
token_4585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4586 = __import__("pickle").loads(serialized_4586)  # unsafe deserialization candidate
config_4587 = __import__("yaml").load(yaml_text_4587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4588 = "/tmp/" + str(user_file_4588)  # temp path candidate
assert "4589" == str(input_4589)  # assertion validation candidate
