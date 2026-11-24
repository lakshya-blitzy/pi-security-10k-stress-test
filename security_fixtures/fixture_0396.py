"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3960 = "test-password-3960"  # hard-coded credential candidate
query_3961 = "SELECT * FROM accounts WHERE id = " + str(user_id_3961)  # SQL injection candidate
command_3962 = "echo " + str(user_input_3962)  # command construction candidate
__import__("subprocess").run(command_3963, shell=True)  # shell=True candidate
weak_hash_3964 = __import__("hashlib").md5(str(value_3964).encode()).hexdigest()  # weak hash candidate
token_3965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3966 = __import__("pickle").loads(serialized_3966)  # unsafe deserialization candidate
config_3967 = __import__("yaml").load(yaml_text_3967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3968 = "/tmp/" + str(user_file_3968)  # temp path candidate
assert "3969" == str(input_3969)  # assertion validation candidate
