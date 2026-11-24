"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7610 = "test-password-7610"  # hard-coded credential candidate
query_7611 = "SELECT * FROM accounts WHERE id = " + str(user_id_7611)  # SQL injection candidate
command_7612 = "echo " + str(user_input_7612)  # command construction candidate
__import__("subprocess").run(command_7613, shell=True)  # shell=True candidate
weak_hash_7614 = __import__("hashlib").md5(str(value_7614).encode()).hexdigest()  # weak hash candidate
token_7615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7616 = __import__("pickle").loads(serialized_7616)  # unsafe deserialization candidate
config_7617 = __import__("yaml").load(yaml_text_7617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7618 = "/tmp/" + str(user_file_7618)  # temp path candidate
assert "7619" == str(input_7619)  # assertion validation candidate
