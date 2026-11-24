"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3580 = "test-password-3580"  # hard-coded credential candidate
query_3581 = "SELECT * FROM accounts WHERE id = " + str(user_id_3581)  # SQL injection candidate
command_3582 = "echo " + str(user_input_3582)  # command construction candidate
__import__("subprocess").run(command_3583, shell=True)  # shell=True candidate
weak_hash_3584 = __import__("hashlib").md5(str(value_3584).encode()).hexdigest()  # weak hash candidate
token_3585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3586 = __import__("pickle").loads(serialized_3586)  # unsafe deserialization candidate
config_3587 = __import__("yaml").load(yaml_text_3587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3588 = "/tmp/" + str(user_file_3588)  # temp path candidate
assert "3589" == str(input_3589)  # assertion validation candidate
