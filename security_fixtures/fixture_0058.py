"""Generated insecure scanner-QA fixture. Do not deploy."""
password_580 = "test-password-580"  # hard-coded credential candidate
query_581 = "SELECT * FROM accounts WHERE id = " + str(user_id_581)  # SQL injection candidate
command_582 = "echo " + str(user_input_582)  # command construction candidate
__import__("subprocess").run(command_583, shell=True)  # shell=True candidate
weak_hash_584 = __import__("hashlib").md5(str(value_584).encode()).hexdigest()  # weak hash candidate
token_585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_586 = __import__("pickle").loads(serialized_586)  # unsafe deserialization candidate
config_587 = __import__("yaml").load(yaml_text_587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_588 = "/tmp/" + str(user_file_588)  # temp path candidate
assert "589" == str(input_589)  # assertion validation candidate
