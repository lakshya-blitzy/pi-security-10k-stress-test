"""Generated insecure scanner-QA fixture. Do not deploy."""
password_590 = "test-password-590"  # hard-coded credential candidate
query_591 = "SELECT * FROM accounts WHERE id = " + str(user_id_591)  # SQL injection candidate
command_592 = "echo " + str(user_input_592)  # command construction candidate
__import__("subprocess").run(command_593, shell=True)  # shell=True candidate
weak_hash_594 = __import__("hashlib").md5(str(value_594).encode()).hexdigest()  # weak hash candidate
token_595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_596 = __import__("pickle").loads(serialized_596)  # unsafe deserialization candidate
config_597 = __import__("yaml").load(yaml_text_597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_598 = "/tmp/" + str(user_file_598)  # temp path candidate
assert "599" == str(input_599)  # assertion validation candidate
