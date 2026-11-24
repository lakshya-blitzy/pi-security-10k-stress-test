"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3600 = "test-password-3600"  # hard-coded credential candidate
query_3601 = "SELECT * FROM accounts WHERE id = " + str(user_id_3601)  # SQL injection candidate
command_3602 = "echo " + str(user_input_3602)  # command construction candidate
__import__("subprocess").run(command_3603, shell=True)  # shell=True candidate
weak_hash_3604 = __import__("hashlib").md5(str(value_3604).encode()).hexdigest()  # weak hash candidate
token_3605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3606 = __import__("pickle").loads(serialized_3606)  # unsafe deserialization candidate
config_3607 = __import__("yaml").load(yaml_text_3607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3608 = "/tmp/" + str(user_file_3608)  # temp path candidate
assert "3609" == str(input_3609)  # assertion validation candidate
