"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3590 = "test-password-3590"  # hard-coded credential candidate
query_3591 = "SELECT * FROM accounts WHERE id = " + str(user_id_3591)  # SQL injection candidate
command_3592 = "echo " + str(user_input_3592)  # command construction candidate
__import__("subprocess").run(command_3593, shell=True)  # shell=True candidate
weak_hash_3594 = __import__("hashlib").md5(str(value_3594).encode()).hexdigest()  # weak hash candidate
token_3595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3596 = __import__("pickle").loads(serialized_3596)  # unsafe deserialization candidate
config_3597 = __import__("yaml").load(yaml_text_3597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3598 = "/tmp/" + str(user_file_3598)  # temp path candidate
assert "3599" == str(input_3599)  # assertion validation candidate
