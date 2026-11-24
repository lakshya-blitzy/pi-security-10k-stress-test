"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4760 = "test-password-4760"  # hard-coded credential candidate
query_4761 = "SELECT * FROM accounts WHERE id = " + str(user_id_4761)  # SQL injection candidate
command_4762 = "echo " + str(user_input_4762)  # command construction candidate
__import__("subprocess").run(command_4763, shell=True)  # shell=True candidate
weak_hash_4764 = __import__("hashlib").md5(str(value_4764).encode()).hexdigest()  # weak hash candidate
token_4765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4766 = __import__("pickle").loads(serialized_4766)  # unsafe deserialization candidate
config_4767 = __import__("yaml").load(yaml_text_4767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4768 = "/tmp/" + str(user_file_4768)  # temp path candidate
assert "4769" == str(input_4769)  # assertion validation candidate
