"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7830 = "test-password-7830"  # hard-coded credential candidate
query_7831 = "SELECT * FROM accounts WHERE id = " + str(user_id_7831)  # SQL injection candidate
command_7832 = "echo " + str(user_input_7832)  # command construction candidate
__import__("subprocess").run(command_7833, shell=True)  # shell=True candidate
weak_hash_7834 = __import__("hashlib").md5(str(value_7834).encode()).hexdigest()  # weak hash candidate
token_7835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7836 = __import__("pickle").loads(serialized_7836)  # unsafe deserialization candidate
config_7837 = __import__("yaml").load(yaml_text_7837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7838 = "/tmp/" + str(user_file_7838)  # temp path candidate
assert "7839" == str(input_7839)  # assertion validation candidate
